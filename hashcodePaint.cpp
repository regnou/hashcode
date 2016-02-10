#include <iostream>
#include <fstream>
#include <utility>
#include <vector>


using namespace std;

/**
 Parses each line for blocks of #, 
 Return : a vector of int pairs, where each pair represents the start and 
 end+1 indexes of a # block.

  e.g. Input :   --###---######-
       Output :  pair<2,5>, pair<8,14>
**/
vector<pair<int,int>>& processLine(vector<pair<int,int>>& aVect, string aLine) {

 
 int p=0, q=0, i=0; 
 int len = aLine.size();

  while (p<len && q<len){
 
    while (i <len && aLine[i] != '#') i++;
    p = i;
    while (i <len && aLine[i] == '#') i++;
    q = i;

     if (p<len && q<len) {
      auto pair = make_pair(p,q);
      aVect.push_back(pair);
     }   
  }

  return aVect;

} //processLine


int main(int argc, char** argv) {

 
  if (argc <= 1) {
    cout << "usage : prog [text file]" << endl;
    return 1;
  }

 ifstream fin;
 char * inFileName = argv[1];

 cout << "opening input file !" << inFileName << endl;
 fin.open(inFileName);

 
 if (!fin.good()) {
  cout << "Error opening input file  1!\n";
  return 1;
  }

 string aLine;

 vector<pair<int,int>> myVect;

 do{
  std::getline(fin,aLine);

  if (aLine.empty() ) continue;
   cout << "[" << aLine << "]" << endl;
   myVect.clear();
   auto v = processLine(myVect,aLine);

   dump<pair<int,int>>(v);

  } while (!fin.eof());

  
} //main
