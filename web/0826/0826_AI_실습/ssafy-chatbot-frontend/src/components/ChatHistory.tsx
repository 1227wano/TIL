import { Alert } from 'react-bootstrap';

function ChatHistory() {
  return (
    <div style={{ flexGrow: 1, overflowY: 'auto', padding: '1rem' }}>
      {/* AI message (left-aligned) */}
      <div className="d-flex justify-content-start mb-3">
        <Alert variant="secondary" style={{ maxWidth: '70%' }}>
          안녕하세요! SSAFY 챗봇입니다. 무엇을 도와드릴까요?
        </Alert>
      </div>

      {/* User message (right-aligned) */}
      <div className="d-flex justify-content-end mb-3">
        <Alert variant="primary" style={{ maxWidth: '70%', backgroundColor: '#00EEFF', borderColor: '#00EEFF', color: '#000' }}>
          React와 TypeScript 프로젝트를 어떻게 시작하나요?
        </Alert>
      </div>
    </div>
  );
}

export default ChatHistory;
