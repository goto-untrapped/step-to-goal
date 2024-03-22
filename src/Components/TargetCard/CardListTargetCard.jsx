import React, { useEffect, useState } from "react";
import axios from "axios";

const CardListTargetCard = ({ style }) => {
  const [targets, setTargets] = useState([]);

  useEffect(() => {
    // データを取得する関数
    const fetchData = async () => {
      try {
        // Pythonのバックエンドからデータを取得
        const targetResponse = await axios.get("/api/target");
        // 取得したデータを状態に設定
        setTargets(targetResponse.data.targets);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    // データを取得する関数を呼び出す
    fetchData();
  }, []); // 最初のレンダリング時にのみ実行される

  console.log("targets size: " + targets.length)

  return (
    targets.length > 0 &&
    targets.map((target, index) => (
      <div class="targetCard cardListTargetCard" style={style}>
        <div class="targetArea">
          <div class="targetTitle">目標</div>
          <div key={index} className="targetContent">
            {target.content}
          </div>
        </div>

        <div class="todoArea">
          <div class="todoTitle">TODO</div>
          {target.todos.length > 0 &&
            target.todos.map((todo, index) => (
              <div key={index} class="todoContent">
                {todo.content}
              </div>
            ))}
        </div>
      </div>
    ))
  );
};

export default CardListTargetCard;
