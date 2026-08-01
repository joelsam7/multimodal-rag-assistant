import { useEffect, useState } from "react";


function Desktop({children}) {

  const [time,setTime] = useState(new Date());


  useEffect(()=>{

    const timer=setInterval(()=>{
      setTime(new Date());
    },1000);

    return ()=>clearInterval(timer);

  },[]);



  return (

    <div
      className="
      h-screen
      bg-[#F1E9DA]
      p-6
      overflow-hidden
      "
    >


      <div
        className="
        h-full
        rounded-3xl
        border-2
        border-[#1A1A1A]
        shadow-[4px_4px_0_#111]
        overflow-hidden
        flex
        flex-col
        "
      >



        <div
          className="
          h-12
          flex-shrink-0
          border-b-2
          border-[#1A1A1A]
          flex
          items-center
          justify-between
          px-5
          font-bold
          "
        >

          <div>
            RAG ASSISTANT
          </div>


          <div className="space-x-6">

            {/* <span>File</span>
            <span>Chat</span>
            <span>Sources</span>
            <span>Help</span> */}

          </div>


          <div>
            {time.toLocaleTimeString()}
          </div>


        </div>





        <div
          className="
          flex
          flex-1
          min-h-0
          overflow-hidden
          "
        >

          {children}

        </div>



      </div>


    </div>

  );
}


export default Desktop;