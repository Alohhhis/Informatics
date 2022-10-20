#include <bits/stdc++.h>

using namespace std;

int main()
{
    const int n=7;
    int s1,s2,s3,s;
    short a[n];
    cout<<"Write 7 digits with 'Enter: '"<<endl;
    for (int i=0;i!=7;i++){
        cin>>a[i];
        if (a[i]!=1 and a[i]!=0){
            cout<<"Write a code in binary!";
        }
    }
        /*
        a[0]=r1
        a[1]=r2
        a[2]=i1
        a[3]=r3
        a[4]=i2
        a[5]=i3
        a[6]=i4
        */
        s1=(a[0]+a[2]+a[4]+a[6])%2;
        s2=(a[1]+a[2]+a[5]+a[6])%2;
        s3=(a[3]+a[4]+a[5]+a[6])%2;
        s=s1*100+s2*10+s3;
        cout<<"Syndrome is: "<<s1<<s2<<s3<<endl;
        if (s==0){
            cout<<"There is no mistakes"<<endl;
            for (int i=0;i!=7;i++){
                cout<<a[i];
            }
            cout<<endl;
        }
        if (s==1){
            a[3]=(a[3]+1)%2;
            cout<<"Mistake in byte (4) r3"<<endl;
            cout<<"Right code is: ";
            for (int i=0;i!=7;i++){
                cout<<a[i];
            }
            cout<<endl;
        }
        if (s==10){
            a[1]=(a[1]+1)%2;
            cout<<"Mistake in byte (2) r2"<<endl;
            cout<<"Right code is: ";
            for (int i=0;i!=7;i++){
                cout<<a[i];
            }
            cout<<endl;
        }
        if (s==11){
            a[5]=(a[5]+1)%2;
            cout<<"Mistake in byte (6) i3"<<endl;
            cout<<"Right code is: ";
            for (int i=0;i!=7;i++){
                cout<<a[i];
            }
            cout<<endl;
        }
        if (s==100){
            a[0]=(a[0]+1)%2;
            cout<<"Mistake in byte (1) r1"<<endl;
            cout<<"Right code is: ";
            for (int i=0;i!=7;i++){
                cout<<a[i];
            }
            cout<<endl;
        }
        if (s==101){
            a[4]=(a[4]+1)%2;
            cout<<"Mistake in byte (5) i2"<<endl;
            cout<<"Right code is: ";
            for (int i=0;i!=7;i++){
                cout<<a[i];
            }
            cout<<endl;
        }
        if (s==110){
            a[2]=(a[2]+1)%2;
            cout<<"Mistake in byte (3) i1"<<endl;
            cout<<"Right code is: ";
            for (int i=0;i!=7;i++){
                cout<<a[i];
            }
            cout<<endl;
        }
        if (s==111){
            a[6]=(a[6]+1)%2;
            cout<<"Mistake in byte (7) i4"<<endl;
            cout<<"Right code is: ";
            for (int i=0;i!=7;i++){
                cout<<a[i];
            }
            cout<<endl;
        }

    cout<<"DONE";
}
