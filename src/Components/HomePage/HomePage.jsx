import React, { useEffect, useState } from 'react'
import EditIcon from '@mui/icons-material/Edit';
import AddIcon from '@mui/icons-material/Add';
import TargetCard from '../TargetCard/TargetCard';
import RegisterModal from '../Register/RegisterModal';
import CardListModal from '../Edit/CardListModal';
import LoginModal from '../Login/LoginModal';
import axios from 'axios';

const HomePage = () => {
    const [openLoginModal, setOpenLoginModal] = React.useState(true);
    const handleOpenLoginModal = () => setOpenLoginModal(true);
    const handleCloseLoginModal = () => setOpenLoginModal(false);

    const [openRegisterModal, setOpenRegisterModal] = React.useState(false);
    const handleOpenRegisterModal = () => setOpenRegisterModal(true);
    const handleCloseRegisterModal = () => setOpenRegisterModal(false);

    const [openCardListModal, setOpenCardListModal] = React.useState(false);
    const handleOpenCardListModal = () => setOpenCardListModal(true);
    const handleCloseCardListModal = () => setOpenCardListModal(false);

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
  
    return (
        <div class="home">
            <div class="homeLeftArea">
                <div 
                class="homeLeftIconArea"
                onClick={handleOpenCardListModal}>
                    <EditIcon class="editIcon"/>
                </div>
            </div>

            <div class="homeCenterArea">
                <TargetCard targets={targets}/>
            </div>

            <div class="homeRightArea">
                <div 
                class="homeRightIconArea"
                onClick={handleOpenRegisterModal}>
                    <AddIcon 
                    class="addIcon" />
                </div>
            </div>

            <section>
                <LoginModal open={openLoginModal} handleClose={handleCloseLoginModal}/>
            </section>
            <section>
                <CardListModal open={openCardListModal} handleClose={handleCloseCardListModal}/>
            </section>
            <section>
                <RegisterModal open={openRegisterModal} handleClose={handleCloseRegisterModal}/>
            </section>
        </div>
    )
}

export default HomePage