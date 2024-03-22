// RegisterModal.js

import axios from 'axios';

const handleRegister = async () => {
    try {
        await axios.post('/api/goals/', { name: goalName, content: goalContent });
        // 登録成功の処理
    } catch (error) {
        // エラーハンドリング
    }
}
