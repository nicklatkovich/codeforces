#include<iostream>
#include<string>
const int g=1000000007;
struct e{
public:
	int c,i;
	e*n,*p;
	bool d;
	e(int _c,int _i=0,e*_n=0,e*_p=0){
		c=_c;
		i=_i;
		n=_n;
		p=_p;
		d=false;
	}
};
using namespace std;
int max(int a,int b){return a<b?a:b;}
int main(){
	e*s=0,*f=0;
	string str;
	int l,*a,r=0;
	cin>>str;
	a=new int[l=str.length()];
	for(int i=0;i<l;i++)a[i]=str[i]-'a';
	for(int i=0,in=1,n=0;i<l;i=in,in++){
		n++;
		if(in==l||a[i]!=a[in]){
			if(s==0)s=f=new e(a[i],n);
			else f=(f->n=new e(a[i],n,0,f));
			n=0;
		}
	}
	while(s!=f){
		int m;
		bool b=true;
		e*i=s;
		while(i){
			int c=i==s||i==f?i->i:(i->i+1)/2;
			m=b||m>c?c:m;
			b=false;
			i=i->n;
		}
		if(b)break;
		r+=m;
		i=s;
		while(i){
			i->i-=i==s||i==f?m:min(i->i,2*m);
			i=i->n;
		}
		i=s;
		while(i){
			if(i->i==0){
				if(i==s)s=s->n;
				else i->p->n=i->n;
				if(i==f)f=f->p;
				else i->n->p=i->p;
			}
			i=i->n;
		}
		i=s;
		while(i){
			if(i->n&&i->c==i->n->c){
				i->i+=i->n->i;
				i->n=i->n->n;
				if(i->n)i->n->p=i;
				else f=i;
			}else i=i->n;
		}
	}
	cout<<r;
}
