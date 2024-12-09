from fastapi import APIRouter, UploadFile, File, HTTPException, status
from app.storage import save_file
import qrcode
from PIL import Image


router = APIRouter()

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    # Lire le contenu du fichier
    file_content = await file.read()

    # Vérifier la taille du fichier (limite de 100 Ko)
    if len(file_content) > 100 * 1024:  # 100 Ko en octets
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail="Fichier trop lourd, limite de 100 Ko"
        )

    # Sauvegarder le fichier
    slug, file_path = save_file(file_content, file.filename)

    # Générer un QR code pointant vers l'URL du fichier
    file_url = f"http://localhost:8000/uploads/{slug}"
    qr_code_path = f"uploads/{slug}.png"
    generate_qr_code(file_url, qr_code_path)

    return {"file_url": file_url, "qr_code_path": qr_code_path}

def generate_qr_code(data, output_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Générer l'image avec les couleurs par défaut (noir sur blanc)
    img = qr.make_image()

    # Sauvegarder l'image
    img.save(output_path)
