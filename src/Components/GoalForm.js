import React, { useState } from 'react';
import axios from 'axios';

const GoalForm = () => {
    const [name, setName] = useState('');
    const [content, setContent] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();  //イベントのデフォルト動作を停止してる
        try {
            await axios.post('/api/goals/', { name, content });   //フォームの内容をサーバーに送信
            alert('Goal created successfully!');
        } catch (error) {
            console.error('Error creating goal:', error);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" value={name} onChange={(e) => setName(e.target.value)} placeholder="Name" />
            <input type="text" value={content} onChange={(e) => setContent(e.target.value)} placeholder="Content" />
            <button type="submit">Submit</button>
        </form>
    );
};

export default GoalForm;
