import React from 'react'
import EditIcon from '@mui/icons-material/Edit';
import AddIcon from '@mui/icons-material/Add';
import TargetCard from '../TargetCard/TargetCard';
import RegisterModal from '../Register/RegisterModal';
import CardListModal from '../Edit/CardListModal';


const HomePage = () => {
    const [openRegisterModal, setOpenRegisterModal] = React.useState(false);
    const handleOpenRegisterModal = () => setOpenRegisterModal(true);
    const handleCloseRegisterModal = () => setOpenRegisterModal(false);

    const [openCardListModal, setOpenCardListModal] = React.useState(false);
    const handleOpenCardListModal = () => setOpenCardListModal(true);
    const handleCloseCardListModal = () => setOpenCardListModal(false);

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
                <TargetCard/>
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
                <CardListModal open={openCardListModal} handleClose={handleCloseCardListModal}/>
            </section>
            <section>
                <RegisterModal open={openRegisterModal} handleClose={handleCloseRegisterModal}/>
            </section>
        </div>
    )
}

export default HomePage