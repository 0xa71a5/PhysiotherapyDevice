#define led 13
#define out 3

#define CONSTANT 0
#define DENSITY_SPACING 1
#define STOPHEADING 2
#define STANDBY 3

#define pulse(x) {digitalWrite(out,1);delayMicroseconds(x);digitalWrite(out,0);}

bool outValue=0;
uint8_t statusReg=255;
uint32_t continueTime=1000;
uint32_t recordTime=0;
uint32_t passTime=0;

int M=20;
int N=5;

int pulseWidth=100;//脉冲宽度us
int pulseBet=2;//脉冲间隔ms
int repeatFrequency=50;//波形重复频率hz
int repeatPeriod=20;//波形重复周期 20ms

void ParseString()
{
  int flag=0;
  String header="";
  int num=0;
  while(Serial.available()!=0)
  {
    char data=Serial.read();
    delay(1);
    if(data=='<')
    {
      flag=1;
    }
    else if(data=='>')
    {
      flag=-1;
      if(header=="P")
      {
        Serial.print("Pulsewidth=");
        Serial.println(num);
        if(num>=10&&num<=1000)
          {
            pulseWidth=num;
          }
      }
      else if(header=="F")
      {
        Serial.print("Frequency=");
        Serial.print(num);
        if(num<=100&&num>=1)
        {
          repeatFrequency=num;
          repeatPeriod=1000/num;
          Serial.print(" Period=");
          Serial.println(repeatPeriod);
        }
      }
      else if(header=="C")
      {
        Serial.print("Mode=");
        Serial.println(num);
        if(num==0)statusReg=CONSTANT;
        else if(num==1)statusReg=DENSITY_SPACING;
        else if(num==2)statusReg=STOPHEADING;
      }
      else if(header=="M")
      {
        Serial.print("M=");
        Serial.println(num);
        if(num<=100&&num>=1)
        {
          M=num;
        }
      }
      else if(header=="N")
      {
        Serial.print("N=");
        Serial.println(num);
        if(num<=100&&num>=1)
        {
          N=num;
        }
      }
      else if(header=="T")
      {
        Serial.print("T=");
        Serial.println(num);
        if(num>=0)
        {
          continueTime=num;
          recordTime=millis();
          passTime=0;
        }
      }
      else if(header=="X")
      {
        Serial.println("Stop!");
        digitalWrite(out,0);
        statusReg=STANDBY;
      }
      else
      {
        Serial.print("Unknow=");
        Serial.println(num);
      }
      header="";
      num=0;
    }
    else if(data==':')
    {
      flag=2;
    }
    else
    {
      if(flag==1)
      {
        header+=char(data);
      }
      else if(flag==2)
      {
        if(data>='0'&&data<='9')
        {
          num*=10;
          num+=data-'0';
        }
      }
    }
  }
}

void StandBy()
{
  while(statusReg==STANDBY)
  {
    if(Serial.available()!=0)ParseString();
  }
}
void ConstantWave()//连续波
{
  int state=1;
  uint32_t lastTime=millis();
  int maxCount=30;
  int count=0;
  while(statusReg==CONSTANT)
  {
    if(Serial.available()!=0)ParseString();
    if(state==1)
    {
      pulse(pulseWidth);
      delayMicroseconds(pulseWidth);
      count++;
      if(count>=maxCount||millis()-lastTime>repeatPeriod)
      {
        state=2;
        count=0;;
      }
    }
    else
    {
      int32_t delayTime=int32_t(repeatPeriod)-(millis()-lastTime);
      if(delayTime>0)
      delay(delayTime);
      state=1;
      lastTime=millis();
    }
  }
}

void DensitySpacingWave()//疎密波
{
  int waitTime1=repeatPeriod/2;
  M=6;
  N=5;
  int waitTimeM=waitTime1/M;
  int waitTimeN=waitTime1/N;
  waitTimeM=pulseWidth;
  waitTimeN=pulseWidth*4;
  int state=1;
  uint32_t lastTime=millis();
  int maxCount=3;
  int count=0;
  while(statusReg==DENSITY_SPACING)
  {
    if(Serial.available()!=0)
    {
      ParseString();
    }
    if(state==1)
    {
      for(int i=0;i<M;i++)
      {
        pulse(pulseWidth);
        delayMicroseconds(waitTimeM);
      }
      for(int i=0;i<N;i++)
      {
        pulse(pulseWidth);
        delayMicroseconds(waitTimeN);
      }
      count++;
      if(count>=maxCount||millis()-lastTime>repeatPeriod)
      {
        state=2;
        count=0;
      } 
    }
    else
    {
      int32_t delayTime=int32_t(repeatPeriod)-(millis()-lastTime);
      if(delayTime>0)
      delay(delayTime);
      state=1;
      lastTime=millis();
    }
  }
}

void StopHeadingWave()
{
  M=10;
  int waitTime1=pulseWidth;
  int waitTime2=M*2*pulseWidth;
  int state=1;
  uint32_t lastTime=millis();
  int maxCount=3;
  int count=0;
  while(statusReg==STOPHEADING)
  {
    if(Serial.available()!=0){
      ParseString();
    }
    if(state==1)
    {
      for(int i=0;i<M;i++)
      {
        pulse(pulseWidth);
        delayMicroseconds(waitTime1);
      }
      delayMicroseconds(waitTime2);
      count++;
      if(count>=maxCount||millis()-lastTime>repeatPeriod)
      {
        state=2;
        count=0;
      }
    }
    else
    {
      int32_t delayTime=int32_t(repeatPeriod)-(millis()-lastTime);
      if(delayTime>0)
      delay(delayTime);
      state=1;
      lastTime=millis();
    }
  }
}

void setup() {
  pinMode(led,OUTPUT);
  pinMode(out,OUTPUT);
  digitalWrite(led,0);
  digitalWrite(out,0);
  Serial.begin(19200);
  statusReg=-1;
}

void loop() {
  StandBy();
  ConstantWave();
  DensitySpacingWave();
  StopHeadingWave();
  if(Serial.available()!=0)ParseString();
}
