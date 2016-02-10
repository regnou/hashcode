#include <iostream>
#include <fstream>
#include <utility>
#include <vector>
#include <sstream>


using namespace std;

void dump(vector<string>& myVect, ofstream& outF) {
  auto iter = myVect.begin();
  while (iter != myVect.end()) {
     outF << *iter++ << endl;
  }
}

void createCmdVect(vector<pair<int,int>>& inpVect, vector<string>& outVect, int row) {

   char str[64];

   for (auto pair : inpVect)  {
     sprintf(str,"PAINT_LINE %d %d %d %d", row, pair.first, row, pair.second);
     string aCmd(str);
     outVect.push_back(aCmd);
   }
}

/**
 Parses each line for blocks of #, 
 Return : a vector of int pairs, where each pair represents the start and 
 end indexes of a # block.

  e.g. Input :   --###---######-
       Output :  pair<2,5>, pair<8,14>
**/
vector<pair<int,int>>& extractHorizontals(vector<pair<int,int>>& aVect, string aLine) {

 
 int p=0, q=0, i=0; 
 int len = aLine.size();

  while (p<len && q<len){
 
    while (i <len && aLine[i] != '#') i++;
    p = i;
    while (i <len && aLine[i] == '#') i++;
    q = i;

     if (p<len && q<len) {
      auto pair = make_pair(p,q-1);
      aVect.push_back(pair);
     }   
  }

  return aVect;

} //extractHorizontals


int main(int argc, char** argv) {

 
  if (argc <= 2) {
    cout << "usage : prog [inpfile] [outfile]" << endl;
    return 1;
  }

 ifstream fin;
 ofstream fout;
 char * inFileName = argv[1];
 char * outFileName = argv[2];

 cout << "opening input file !" << inFileName << endl;
 fin.open(inFileName);

 
 if (!fin.good()) {
  cout << "Error opening input file  1!\n";
  return 1;
  }



 string aLine;


 std::getline(fin,aLine);
 istringstream readStr(aLine);
 
 int rows, cols;
 readStr >> rows >> cols;

 vector<pair<int,int>> rawVect;
 vector<string> cmdVect;

 int r = 0;
 do{
  std::getline(fin,aLine);

  if (aLine.empty() ) continue;
   cout << "[" << aLine << "]" << endl;
   rawVect.clear();
   auto v = extractHorizontals(rawVect,aLine);

   createCmdVect(rawVect, cmdVect, r);
   //dump<pair<int,int>>(v);

   r++;
  } while (!fin.eof());

  cout << "cmdVect.size: "  <<  cmdVect.size() << endl;

  cout << "opening input file !" << inFileName << endl;
  fout.open(outFileName);
  fout <<  cmdVect.size() << endl;

  dump(cmdVect, fout);

  fout.close();

} //main
