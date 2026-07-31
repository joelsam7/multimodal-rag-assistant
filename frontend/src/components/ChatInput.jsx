import {
  Plus,
  Send,
  X
} from "lucide-react";


function ChatInput({
  message,
  setMessage,
  sendMessage,
  handleFile,
  loading,
  selectedImage,
  setSelectedImage,
  fileInputRef
}) {


  return (

    <>


      {
        selectedImage && (

          <div
            className="
            border
            p-2
            rounded-lg
            mb-3
            flex
            justify-between
            "
          >

            <span>
              {selectedImage.name}
            </span>


            <button
              onClick={() => setSelectedImage(null)}
            >
              <X/>
            </button>


          </div>

        )
      }



      <div
        className="
        flex
        gap-3
        border-2
        rounded-xl
        p-3
        "
      >


        <input
          type="file"
          hidden
          ref={fileInputRef}
          onChange={handleFile}
        />


        <button
          onClick={() =>
            fileInputRef.current.click()
          }
        >

          <Plus/>

        </button>



        <input

          className="
          flex-1
          bg-transparent
          outline-none
          "

          placeholder="Ask your knowledge base..."

          value={message}

          onChange={(e)=>
            setMessage(e.target.value)
          }

          onKeyDown={(e)=>{
            if(e.key==="Enter"){
              sendMessage();
            }
          }}

        />



        <button
          disabled={loading}
          onClick={sendMessage}
        >

          <Send/>

        </button>


      </div>


    </>

  );
}


export default ChatInput;