import { Link } from 'react-router-dom';
import { Navbar, Nav, Container, Button } from 'react-bootstrap';

function AppNavbar() {
  return (
    <Navbar bg="dark" variant="dark" expand="lg" className="shadow-sm">
      <Container>
        <Navbar.Brand as={Link} to="/" style={{ color: '#00EEFF' }}>
          SSAFY
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="ms-auto align-items-center">
            <Nav.Link as={Link} to="/chat">채팅</Nav.Link>
            <Nav.Link as={Link} to="/login">로그인</Nav.Link>
            <Button variant="primary" as={Link} to="/signup" className="ms-lg-2 mt-2 mt-lg-0">
              회원가입
            </Button>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default AppNavbar;