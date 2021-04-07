import { useEffect, useRef, useState } from "react";
import {Container, Col, Row} from 'reactstrap';


import socketIOClient from "socket.io-client";

const NEW_CHAT_MESSAGE_EVENT = "newChatMessage";
const SOCKET_SERVER_URL = "http://localhost:5000";


// const useChat: React.FunctionComponent<number> = (roomId) => {
//   const [messages, setMessages] = useState([]);
//   const socketRef:any = useRef();

//   useEffect(() => {
    
//     // Creates a WebSocket connection
//     socketRef.current:any = socketIOClient(SOCKET_SERVER_URL, {
//       query: { roomId },
//     });
    
//     // Listens for incoming messages
//     socketRef.current.on(NEW_CHAT_MESSAGE_EVENT, (message) => {
//       const incomingMessage = {
//         ...message,
//         ownedByCurrentUser: message.senderId === socketRef.current.id,
//       };
//       setMessages((messages) => [...messages, incomingMessage]);
//     });
    
//     // Destroys the socket reference
//     // when the connection is closed
//     return () => {
//       socketRef.current.disconnect();
//     };
//   }, [roomId]);

//   // Sends a message to the server that
//   // forwards it to all users in the same room
//   const sendMessage = (messageBody) => {
//     socketRef.current.emit(NEW_CHAT_MESSAGE_EVENT, {
//       body: messageBody,
//       senderId: socketRef.current.id,
//     });
//   };

//   return { messages, sendMessage };
// };

const Home = () =>{
    return (<div>home page</div>)
}

export default Home;