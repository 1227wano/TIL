import { Container, Form, Button, Card } from 'react-bootstrap';
import { Link } from 'react-router-dom';

function SignupPage() {
  return (
    <Container className="mt-5 d-flex justify-content-center">
      <Card style={{ width: '30rem' }}>
        <Card.Body>
          <Card.Title className="text-center mb-4">회원가입</Card.Title>
          <Form>
            <Form.Group className="mb-3" controlId="formBasicName">
              <Form.Label>이름</Form.Label>
              <Form.Control type="text" placeholder="이름을 입력하세요" />
            </Form.Group>

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
                    회원가입
                </Button>
            </div>
          </Form>
          <div className="mt-3 text-center">
            이미 계정이 있으신가요? <Link to="/login">로그인</Link>
          </div>
        </Card.Body>
      </Card>
    </Container>
  );
}

export default SignupPage;