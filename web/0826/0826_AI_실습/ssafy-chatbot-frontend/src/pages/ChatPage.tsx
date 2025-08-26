import { Container } from 'react-bootstrap';
import ChatHistory from '../components/ChatHistory';
import MessageInput from '../components/MessageInput';

function ChatPage() {
  return (
    <Container fluid style={{ height: 'calc(100vh - 56px)', display: 'flex', flexDirection: 'column', padding: 0 }}>
      <ChatHistory />
      <MessageInput />
    </Container>
  );
}

export default ChatPage;