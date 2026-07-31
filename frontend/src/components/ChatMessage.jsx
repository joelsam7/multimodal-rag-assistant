import ReactMarkdown from "react-markdown";

function ChatMessage({
  message
}) {

  return (

    <div
      className={`
      max-w-3xl
      p-4
      rounded-xl
      border-2

      ${
        message.role === "user"
        ?
        "ml-auto bg-[#8FD1C6]"
        :
        "bg-[#DDD6FE]"
      }

      `}
    >


      <p className="font-bold mb-2">

        {
          message.role === "user"
          ?
          "You"
          :
          "Assistant"
        }

      </p>


      <ReactMarkdown>
        {message.text}
      </ReactMarkdown>  



      {
        message.sources && (

          <div
            className="
            mt-4
            text-sm
            border-t
            pt-2
            "
          >

            Sources:

            {
              message.sources.map((s,index)=>(

                <div key={index}>
                  {s.source} - page {s.page}
                </div>

              ))
            }

          </div>

        )
      }


    </div>

  );
}


export default ChatMessage;