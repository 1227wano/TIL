import { Form, Button, InputGroup } from 'react-bootstrap';

function MessageInput() {
  return (
    <div style={{ padding: '1rem', backgroundColor: '#f8f9fa' }}>
      <InputGroup>
        <Button variant="outline-secondary">
          🖼️
        </Button>
        <Form.Control
          placeholder="질문을 입력하세요..."
          aria-label="User question"
        />
        <Button style={{ backgroundColor: '#00EEFF', borderColor: '#00EEFF' }}>
          전송
        </Button>
      </InputGroup>
    </div>
  );
}

export default MessageInput;
