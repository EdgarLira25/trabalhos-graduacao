import axios from 'axios';

const api = axios.create({
    baseURL: 'https://backend-imdb.azurewebsites.net',
    headers: {
        'Content-Type': 'application/json',
        "ngrok-skip-browser-warning": "69420"
    }

});

export default api;
