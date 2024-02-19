from PIL import Image

def rotate_image(input_path, output_path, degrees):
    # 이미지 열기
    image = Image.open(input_path)

    # 이미지 회전
    rotated_image = image.rotate(degrees)

    # 회전된 이미지 저장
    rotated_image.save(output_path)

if __name__ == "__main__":
    # 입력 파일 경로 및 출력 파일 경로 설정
    input_file = "27.jpg"
    output_file = "27_1.jpg"

    # 7도만큼 회전
    rotation_angle = -5

    # 이미지 회전 함수 호출
    rotate_image(input_file, output_file, rotation_angle)

    print(f"이미지가 {rotation_angle}도만큼 회전되었습니다.")
