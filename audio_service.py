import nemo.collections.asr as nemo_asr
from infer import infer_greedy
from settings import MODEL_PATH


class AudioService:
    def __init__(self) -> None:
        self.asr_model = nemo_asr.models.EncDecCTCModel.restore_from(MODEL_PATH)

    # Извлечение текста из аудиофайла
    def get_text_from_audio(self, filepath: str) -> str:
        files = [filepath]
        return infer_greedy(files, self.asr_model)[0]
