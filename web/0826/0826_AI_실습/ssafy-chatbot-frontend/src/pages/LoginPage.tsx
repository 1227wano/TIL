import { Container, Form, Button, Card } from 'react-bootstrap';
import { Link } from 'react-router-dom';

function LoginPage() {
  return (
    <Container className="mt-5 d-flex justify-content-center">
      <Card style={{ width: '30rem' }}>
        <Card.Body>
          <Card.Title className="text-center mb-4">로그인</Card.Title>
          <Form>
            <Form.Group className="mb-3" controlId="formBasicEmail">
              <Form.Label>이메일 주소</Form.Label>
              <Form.Control type="email" placeholder="이메일을 입력하세요" />
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicPassword">
              <Form.Label>비밀번호</Form.Label>
              <Form.Control type="password" placeholder="비밀번호를 입력하세요" />
            </Form.Group>
            
            <div className="d-grid">
                <Button variant="primary" type="submit">
                    로그인
                </Button>
            </div>
          </Form>
          <div className="mt-3 text-center">
            계정이 없으신가요? <Link to="/signup">회원가입</Link>
          </div>
        </Card.Body>
      </Card>
    </Container>
  );
}

export default LoginPage;