#include<iostream>
#include<string>
const int g=1000000007;
struct e{
public:
	int i;
	e*n;
	e*p;
	bool d;
	e(int _i=0,e*_n=0,e*_p=0){
		i=_i;
		n=_n;
		p=_p;
		d=false;
	}
};
using namespace std;
int main(){
	e*s=0,*f=0;
	string str;
	cin>>str;
	int l=str.length();
	for(int i=0;i<l;i++){
		if(i==0)s=f=new e(str[i]-'a',0,0);
		else f=((f->n=new e(str[i]-'a',0,f))->p=f)->n;
	}
	int r=0;
	while(true){
		bool _break=true;
		e*i=s;
		while(i){
			if((i->p&&i->p->i!=i->i)||(i->n&&i->n->i!=i->i)){
				i->d=true;
				_break=false;
			}
			i=i->n;
		}
		if(_break)break;
		i = s;
		while(i){
			if(i->d){
				if(i->p)i->p->n=i->n;
				if(i->n)i->n->p=i->p;
			}
			i=i->n;
		}
		r++;
		while(s&&s->d)s=s->n;
	}
	cout<<r;
}
