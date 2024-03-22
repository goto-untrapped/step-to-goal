import Modal from "@mui/material/Modal";
import * as React from "react";
import { IconButton } from "@mui/material";
import CloseIcon from "@mui/icons-material/Close";
import EditCardModal from "./EditCardModal";
import styles from "./CardListCardStyle.css";
import CardListTargetCard from "../TargetCard/CardListTargetCard";

export default function CardListModal({ handleClose, open }) {
  const [openEditCardModal, setOpenEditCardModal] = React.useState(false);
  const handleOpenEditCardModal = () => setOpenEditCardModal(true);
  const handleCloseEditCardModal = () => setOpenEditCardModal(false);

  return (
    <div>
      <Modal
        open={open}
        onClose={handleClose}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <div class="cardListModal">
          <div class="cardListModalTitle">
            <IconButton onClick={handleClose} aria-label="delete">
              <CloseIcon />
            </IconButton>
            目標一覧
          </div>
          <div class="cardListArea">
            <div 
            onClick={handleOpenEditCardModal}>
                <CardListTargetCard />
            </div>
          </div>

          <section>
            <EditCardModal
              open={openEditCardModal}
              handleClose={handleCloseEditCardModal}
            />
          </section>
        </div>
      </Modal>
    </div>
  );
}
