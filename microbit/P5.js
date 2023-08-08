// [변경1] 티처블 머신, 시리얼포트 변경하기
// 티처블 머신에서 생성한 모델 URL 넣기
const modelURL = 'https://teachablemachine.withgoogle.com/models/wQ_b8kB-U/';
// 마이크로비트와 연결된 시리얼 포트 넣기
const serialPort = 'COM9';

let classifier;
let serial;
let video;
let flippedVideo;
let label;

function preload() {
    classifier = ml5.imageClassifier(modelURL + 'model.json');
    serial = new p5.SerialPort();
}

function setup() {
    serial.open(serialPort);
    createCanvas(320, 260);
    video = createCapture(VIDEO);
    video.size(320, 240);
    video.hide();
    flippedVideo = ml5.flipImage(video);
    classifyVideo();
}

function draw() {
    background(0);
    image(flippedVideo, 0, 0);
    fill(255);
    textSize(16);
    textAlign(CENTER);
    text(label, width / 2, height - 4);
}

function classifyVideo() {
    flippedVideo = ml5.flipImage(video)
    classifier.classify(flippedVideo, gotResult);
    flippedVideo.remove();
}

function gotResult(error, results) {
    if (error) {
        console.error(error);
        return;
    }
    label = String(results[0].label);
  // [변경2] 티처블 머신 AI 분류 결과("클래스명")를 시리얼 통신으로 전송
    console.log(label);   // 콘솔창에 AI 분류 결과 출력("클래스명")
    serial.write(label);
    classifyVideo();
}