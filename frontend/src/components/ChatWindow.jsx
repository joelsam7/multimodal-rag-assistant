import ChatMessage from "./ChatMessage";
import { useEffect, useRef } from "react";

function ChatWindow({
  messages,
  loading
}) {

  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({
      behavior: "smooth"
    });
  }, [messages, loading]);


  return (

    <div
      className="
      flex-1
      overflow-y-auto
      space-y-4
      min-h-0
      "
    >

      {
        messages.length === 0 && (

          <div
            className="
            mx-auto
            mt-20
            w-[450px]
            border-2
            rounded-xl
            shadow-[4px_4px_0_#111]
            p-8
            text-center
            "
          >

            <h1
              className="
              text-3xl
              font-bold
              "
            >
              Welcome!
            </h1>


            <p className="mt-3">
              Ask anything about your documents
            </p>


          </div>

        )
      }



      {
        messages.map((msg, index) => (

          <ChatMessage
            key={index}
            message={msg}
          />

        ))
      }



      {
        loading && (

          <div>
            Thinking...
          </div>

        )
      }


      {/* Auto scroll target */}
      <div ref={bottomRef}></div>


    </div>

  );
}


export default ChatWindow;