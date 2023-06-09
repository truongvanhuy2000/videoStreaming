import grpc
import cv2

from webServer.proto import image_pb2, image_pb2_grpc
from webServer.common.helper import deserializeTheImage
from webServer.transportation.protocol.clientProtocol import clientProtocol
from webServer.common import logger

class grpcClient(clientProtocol):
    def __init__(self) -> None:
        super().__init__()

    def request(self, video, model, addr):
        logger._LOGGER.info(f"Try connect to: {addr}")
        channel_opt = [
                ("grpc.so_reuseport", 1),
                ("grpc.use_local_subchannel_pool", 1)
            ]
        with grpc.insecure_channel(addr, options=channel_opt) as channel:
            logger._LOGGER.info(f"Start Requesting image")
            stub = image_pb2_grpc.image_tranferStub(channel=channel)
            response = stub.send_me_image(image_pb2.image_request(model=model, video=video))
            try:
                for img in response:
                    frame = deserializeTheImage(img.image_sent.data)
                    ret, buffer = cv2.imencode('.jpg', frame)
                    frame = buffer.tobytes()
                    # Yield the frame in byte format
                    yield (b'--frame\r\n'
                        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            except:
                response.cancel()
                logger._LOGGER.info("Done Streaming")
                stub.ack(image_pb2.ack_request(req="done video"))

    def response(self):
        print("do nothing")
        pass


            