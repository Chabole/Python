//Programa : Teste MPU6050 e LCD 20x4
//Alteracoes e adaptacoes : FILIPEFLOP
//
//Baseado no programa original de JohnChi
 
//Carrega a biblioteca Wire
#include<Wire.h>
 
//Endereco I2C do MPU6050
const int MPU=0x68;  

//Variaveis para armazenar valores dos sensores
int AcX,AcY,AcZ;


void setup()
{
  //Transmissão serial
  Serial.begin(115200);
     
  //Inicializa o MPU-6050
  Wire.write(0); 
  Wire.endTransmission(true); 

  Serial.print("AcX");
  Serial.print("\t"); Serial.print("AcY");
  Serial.print("\t"); Serial.println("AcZ");
}
void loop()
{
  Wire.beginTransmission(MPU);
  Wire.write(0x3B);  // starting with register 0x3B (ACCEL_XOUT_H)
  Wire.endTransmission(false);
  
  //Solicita os dados do sensor
  Wire.requestFrom(MPU,14,true);  
  //Armazena o valor dos sensores nas variaveis correspondentes
  AcX=Wire.read()<<8|Wire.read();  //0x3B (ACCEL_XOUT_H) & 0x3C (ACCEL_XOUT_L)     
  AcY=Wire.read()<<8|Wire.read();  //0x3D (ACCEL_YOUT_H) & 0x3E (ACCEL_YOUT_L)
  AcZ=Wire.read()<<8|Wire.read();  //0x3F (ACCEL_ZOUT_H) & 0x40 (ACCEL_ZOUT_L)
    
  //Envia valor X do acelerometro para a serial e o LCD
  Serial.print(""); Serial.print(AcX);
   
  //Envia valor Y do acelerometro para a serial e o LCD
  Serial.print("\t"); Serial.print(AcY);
  
  //Envia valor Z do acelerometro para a serial e o LCD
  Serial.print("\t"); Serial.println(AcZ);
  
  //Aguarda 300 ms e reinicia o processo
  delay(10);
}
