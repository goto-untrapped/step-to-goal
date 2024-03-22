
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const GoalList = () => {
    const [goals, setGoals] = useState([]);

    useEffect(() => {
        const fetchGoals = async () => {
            try {
                const response = await axios.get('/api/goals/');
                setGoals(response.data);
            } catch (error) {
                console.error('Error fetching goals:', error);
            }
        };
        fetchGoals();
    }, []);

    return (
        <div>
            <h2>Goals</h2>
            <ul>
                {goals.map((goal) => (
                    <li key={goal.id}>
                        <h3>{goal.name}</h3>
                        <p>{goal.content}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default GoalList;
