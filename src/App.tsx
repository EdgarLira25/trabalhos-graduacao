import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import Header from './components/header';
import SqlQuery from './pages/SqlQuery/SqlQuery';

function App() {
    return (
        <Router>
            <Header></Header>
            <Routes>
                <Route path="/query" element={<SqlQuery />} />
                <Route path="/" element={<Navigate to="/query" />} />
            </Routes>
        </Router>
    );
}

export default App;
