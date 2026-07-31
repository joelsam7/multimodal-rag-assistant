import { useEffect, useRef, useState } from "react";

import Desktop from "../components/Desktop";
import Sidebar from "../components/Sidebar";
import ChatWindow from "../components/ChatWindow";
import ChatInput from "../components/ChatInput";

import {
  askQuestion,
  uploadFile,
  imageChat,
  getDocuments
} from "../services/api";

function Home() {


  const [message,setMessage] = useState("");

  const [messages,setMessages] = useState([]);

  const [loading,setLoading] = useState(false);

  const [documents,setDocuments] = useState([]);

  const [selectedImage,setSelectedImage] = useState(null);

  const [activePanel,setActivePanel] = useState(null);



  const fileInputRef = useRef(null);



  // Load history
  useEffect(()=>{

    const saved =
      localStorage.getItem("ragHistory");


    if(saved){

      setHistory(JSON.parse(saved));

    }

  },[]);



  // Save history
  useEffect(()=>{

    localStorage.setItem(
      "ragHistory",
      JSON.stringify(history)
    );

  },[history]);



  useEffect(()=>{

    loadDocuments();

  },[]);



  const loadDocuments = async()=>{

    try{

      const res = await getDocuments();

      setDocuments(
        res.data.documents || []
      );

    }
    catch(err){

      console.log(err);

    }

  };





  const handleFile = async(e)=>{


    const file = e.target.files[0];

    if(!file) return;



    const imageTypes=[
      "image/png",
      "image/jpeg",
      "image/jpg"
    ];



    if(imageTypes.includes(file.type)){


      setSelectedImage(file);


      setMessages(prev=>[
        ...prev,
        {
          role:"system",
          text:`Image attached: ${file.name}`
        }
      ]);


      return;

    }




    try{

      setLoading(true);


      const res =
        await uploadFile(file);



      setMessages(prev=>[
        ...prev,
        {
          role:"assistant",
          text:
          `Uploaded ${res.data.filename} successfully.`
        }
      ]);

      loadDocuments();


    }
    catch(err){

      setMessages(prev=>[
        ...prev,
        {
          role:"assistant",
          text:"Upload failed."
        }
      ]);

    }
    finally{

      setLoading(false);

    }


  };






  const sendMessage = async()=>{


    if(!message.trim())
      return;



    const question = message;



    setMessages(prev=>[
      ...prev,
      {
        role:"user",
        text:question
      }
    ]);



    setMessage("");

    setLoading(true);



    try{


      if(selectedImage){


        const res =
          await imageChat(
            selectedImage,
            question
          );



        setMessages(prev=>[
          ...prev,
          {
            role:"assistant",
            text:res.data.answer
          }
        ]);


        setSelectedImage(null);


      }

      else{


        const res =
          await askQuestion(question);



        setMessages(prev=>[
          ...prev,
          {
            role:"assistant",
            text:res.data.answer,
            sources:res.data.sources
          }
        ]);

      }


    }
    catch(err){


      setMessages(prev=>[
        ...prev,
        {
          role:"assistant",
          text:"Server error. Check backend connection."
        }
      ]);


    }
    finally{

      setLoading(false);

    }


  };






  const newChat = ()=>{


    if(messages.length > 0){


      setHistory(prev=>[

        ...prev,

        messages

      ]);


    }



    setMessages([]);

    setSelectedImage(null);

    setMessage("");

  };







  return (


    <Desktop>


      <Sidebar

        onNewChat={newChat}

        onDocuments={()=>setActivePanel("documents")}

        onHistory={()=>setActivePanel("history")}

        onSettings={()=>setActivePanel("settings")}

        documents={documents}

      />




      <main
      className="
      flex-1
      flex
      flex-col
      p-8
      overflow-hidden
      min-h-0
      "
      >



        <ChatWindow

          messages={messages}

          loading={loading}

        />




        <ChatInput

          message={message}

          setMessage={setMessage}

          sendMessage={sendMessage}

          handleFile={handleFile}

          loading={loading}

          selectedImage={selectedImage}

          setSelectedImage={setSelectedImage}

          fileInputRef={fileInputRef}

        />





        {
          activePanel && (


          <div
          className="
          absolute
          right-10
          top-20
          bg-[#F5EEFF]
          text-black
          border-2
          rounded-xl
          p-5
          shadow-[4px_4px_0_#111]
          w-80
          "
          >



          <button
          className="float-right"
          onClick={()=>setActivePanel(null)}
          >
          ✕
          </button>





          {
          activePanel==="documents" && (

          <>

          <h2 className="font-bold text-xl">
          Documents
          </h2>


          {
          documents.map((doc,i)=>(

          <p key={i} className="mt-2">
          📄 {doc}
          </p>

          ))
          }

          </>

          )
          }






          {
          activePanel==="history" && (

          <>

          <h2 className="font-bold text-xl">
          History
          </h2>


          {
          history.length===0 ?


          <p className="mt-3">
          No previous chats yet.
          </p>


          :


          history.map((chat,index)=>(

          <div
          key={index}
          className="mt-3 border p-2 rounded"
          >

          Chat {index+1}

          <p>
          {chat[0]?.text}
          </p>


          </div>


          ))

          }


          </>

          )
          }






          {
          activePanel==="settings" && (

          <>

          <h2 className="font-bold text-xl">
          Settings
          </h2>


          <p className="mt-3">
          Backend:
          http://127.0.0.1:8000
          </p>

          </>

          )
          }



          </div>


          )

        }



      </main>



    </Desktop>


  );

}


export default Home;