import cv2
from pyzbar.pyzbar import decode

def read_qr_code(image_path):
    # 이미지 로드
    image = cv2.imread(image_path)

    # QR 코드 디코드
    decoded_objects = decode(image)

    # 디코드된 정보 출력
    for obj in decoded_objects:
        print(f'Type: {obj.type}')
        print(f'Data: {obj.data}')
        print()

        # (Optional) 이미지에 사각형 그리기
        points = obj.polygon
        if len(points) == 4:
            pts = []
            for point in points:
                pts.append([point.x, point.y])
            pts = int0(pts)
            cv2.polylines(image, [pts], isClosed=True, color=(0, 255, 0), thickness=2)

    # 결과 이미지 보기
    cv2.imshow('QR Code Reader', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = "21.jpg"  # 이미지 파일 경로 설정
    read_qr_code(image_path)
