import {
  FileText,
  History,
  Settings,
  Plus
} from "lucide-react";


function Sidebar({
  onNewChat,
  
  onDocuments,
  onHistory,
  onSettings,
  documents
}) {

  return (

      <aside
      className="
      w-60
      bg-[#1A1A1A]
      text-[#F1E9DA]
      p-5
      h-full
      overflow-y-auto
      flex-shrink-0
      "
      >

      <button
        onClick={onNewChat}
        className="
        flex
        items-center
        gap-3
        border
        rounded-lg
        p-3
        w-full
        hover:bg-white/10
        mb-5
        "
      >

        <Plus size={18}/>
        New Chat

      </button>



      <div className="space-y-5">


        <button
          onClick={onDocuments}
          className="
          flex
          items-center
          gap-3
          w-full
          "
        >

          <FileText size={18}/>
          Documents

        </button>




        <button
          onClick={onHistory}
          className="
          flex
          items-center
          gap-3
          w-full
          "
        >

          <History size={18}/>
          History

        </button>





        <button
          onClick={onSettings}
          className="
          flex
          items-center
          gap-3
          w-full
          "
        >

          <Settings size={18}/>
          Settings

        </button>


      </div>



    </aside>

  );
}


export default Sidebar;     