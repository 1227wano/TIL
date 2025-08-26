import { Container, Button } from 'react-bootstrap';
import { Link } from 'react-router-dom';

function LandingPage() {
  return (
    <Container className="mt-5 text-center">
      <h1>SSAFY 챗봇 서비스</h1>
      <p className="lead">AI와 대화하고 질문하세요. 텍스트와 이미지를 모두 지원합니다.</p>
      <hr />
      <p>gpt-5-nano 모델을 기반으로 가장 정확한 답변을 제공합니다.</p>
      <Button variant="primary" size="lg" as={Link} to="/chat">
        채팅 시작하기
      </Button>
    </Container>
  );
}

export default LandingPage;