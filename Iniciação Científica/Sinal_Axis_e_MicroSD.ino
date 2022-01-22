//Programa: Teste MPU6050 e Gravação em SD
//Alteracoes e adaptacoes : Arthur Chabole
//
//Baseado no programa original de JohnChi e FILIPEFLOP
 
//Carrega a biblioteca Wire
#include<Wire.h>
//Carregar biblioteca SD
#include<SD.h>
 
//Endereco I2C do MPU6050
const int MPU=0x68;  

//Variaveis para armazenar valores dos sensores e iniciando contador c
int AcX,AcY,AcZ;
double c=0;

//Configurando a análi1e
String Name_file= ("A4_A.txt");  //Nome do arquivo
double Max= 5000;                //Número Max de pontos
int t= 2;                       //Tempo de delay

void setup()
{ 
  //Transmissão serial
  Serial.begin(115200);

  //Configurando SD
  SD.begin(4);

  //Zerando acelerômetro
  Wire.begin();
  Wire.beginTransmission(MPU);
  Wire.write(0x6B); 
 
  //Inicializa o MPU-6050
  Wire.write(0); 
  Wire.endTransmission(true); 

  Serial.print("AcX");
  Serial.print("\t"); Serial.print("AcY");
  Serial.print("\t"); Serial.println("AcZ");

  /*
  File dados = SD.open(Name_file,FILE_WRITE);
  dados.print("x"); dados.print("\t");
  dados.print("AcX"); dados.print("\t");
  dados.print("AcY"); dados.print("\t");
  dados.println("AcZ");
  dados.close();
  */
}
void loop()
{
  //Número de pontos de análise
  while (c>Max);
  {
  //Iniciando comunicação com sensor
  Wire.beginTransmission(MPU);
  Wire.write(0x3B);  // starting with register 0x3B (ACCEL_XOUT_H)
  Wire.endTransmission(false);
  
  //Solicita os dados do sensor
  Wire.requestFrom(MPU,14,true);  
  //Armazena o valor dos sensores nas variaveis correspondentes
  AcX=Wire.read()<<8|Wire.read();  //0x3B (ACCEL_XOUT_H) & 0x3C (ACCEL_XOUT_L)     
  AcY=Wire.read()<<8|Wire.read();  //0x3D (ACCEL_YOUT_H) & 0x3E (ACCEL_YOUT_L)
  AcZ=Wire.read()<<8|Wire.read();  //0x3F (ACCEL_ZOUT_H) & 0x40 (ACCEL_ZOUT_L)

  //Gravando no cartão
  File dados = SD.open(Name_file,FILE_WRITE);
  if (dados){
    dados.print(c); dados.print("\t");
    dados.print(AcX); dados.print("\t");
    dados.print(AcY); dados.print("\t");
    dados.println(AcZ);
    c += 1; 
    dados.close();
  } else{
    Serial.println("Erro ao criar o arquivo");
  }
    
  //Envia valor X do acelerometro para a serial e o LCD
  Serial.print(""); Serial.print(AcX);
   
  //Envia valor Y do acelerometro para a serial e o LCD
  Serial.print("\t"); Serial.print(AcY);
  
  //Envia valor Z do acelerometro para a serial e o LCD
  Serial.print("\t"); Serial.println(AcZ);
  
  //Aguarda 300 ms e reinicia o processo
  delay(t);
  }
}
