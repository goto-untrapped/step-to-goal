import React from 'react';

const GoalData = ({ goals }) => {
  return (
    <div>
      <h1>Goal data</h1>
      <ul>
        {goals.map((goal, index) => (
          <li key={index}>{goal.name} - {goal.content}</li>
        ))}
      </ul>
    </div>
  );
}

export default GoalData;
