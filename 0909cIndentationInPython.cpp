#include<iostream>
const int g=1000000007;
struct e{
public:
	int i;
	e*n;
	e(int k=0){
		i=k;
		n=0;
	}
};
using namespace std;
int main(){
	int n;
	cin>>n;
	e*s=new e(1),*l=s;
	bool p=true;
	for(int i=0;i<n;i++){
		if(p){
			e*j=s->n,*k=s;
			while(j){
				j->i=(j->i+k->i)%g;
				j=(k=j)->n;
			}
		}else l=(l->n=new e());
		char c;
		cin>>c;
		p=c=='s';
	}
	e*j=s;
	int result=0;
	while(j){
		result=(result+j->i)%g;
		j=j->n;
	}
	cout<<result;
}
