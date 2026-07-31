const KEY = "rag_chats";


// Load all saved chats
export function loadChats() {

  const data = localStorage.getItem(KEY);

  return data
    ? JSON.parse(data)
    : [];

}


// Save all chats
export function saveChats(chats) {

  localStorage.setItem(
    KEY,
    JSON.stringify(chats)
  );

}


// Create a new chat object
export function createChat() {

  return {

    id: Date.now(),

    title: "New Chat",

    messages: []

  };

}