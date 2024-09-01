import SqlQuery from './pages/SqlQuery';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/header';

function App() {
    return (
        <Router>
            <Header></Header>
            <Routes>
                <Route path="/query" element={<SqlQuery />} />
            </Routes>
        </Router>
    );
}

export default App;
