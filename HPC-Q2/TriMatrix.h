//
//  TriMatrix.h
//  HPC-Q2
//
//  Created by hyo13 on 22/3/16.
//  Copyright (c) 2016 hyo13. All rights reserved.
//

#ifndef CLASS_TriMatrix
#define CLASS_TriMatrix

#include <stdio.h>
#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

class TriMatrix{
    
private:
    vector <double> *diagm, *diagu, *diagl;
    
public:
    TriMatrix(double v,double size){
        diagm = new vector <double> (size);
        diagu = new vector <double> (size-1);
        diagl = new vector <double> (size-1);
        
        //create diagm vector
        (*diagm)[0]=1;
        (*diagm)[size-1]=1;
        for (int i=1;i<size-1;i++){
            (*diagm)[i]=1-2*v;
        }
        
        //create diagu vector
        (*diagu)[0]=0;
        for (int i=1;i<size-1;i++){
            (*diagu)[i]=v;
        }
        
        //create diagl vector
        (*diagl)[size-2]=0;
        for (int i=0;i<size-2;i++){
            (*diagl)[i]=v;
        }
        
    }
    
    vector<double> operator* (vector<double> X){
        double s=X.size();
        
        //diagm multiply X
        vector<double> Am(s);
        for (int i=0;i<s;i++){
            Am[i]=(*diagm)[i]*X[i];
        }
        
        //diagu multiply X
        vector<double> Au(s);
        for (int i=0;i<s-1;i++){
            Au[i]=(*diagu)[i]*X[i+1];
        }
        Au[s-1]=0;
        
        //diagl multiply X
        vector<double> Al(s);
        Al[0]=0;
        for (int i=1;i<s;i++){
            Al[i]=(*diagl)[i-1]*X[i-1];
        }
        
        //Superposition of Results
        vector<double> B(s);
        for (int i=0;i<s;i++){
            B[i]=Am[i]+Au[i]+Al[i];
        }
        return B;
    }
};


#endif /* defined(__HPC_Q1__TriMatrix__) */
