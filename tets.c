#include <stdio.h>
#include<unistd.h> 


// int main() {
//   int status;
//   pid_t pid; 
//   if (fork() == 0) {
//     printf("A");
//     fflush(stdout);

//     if (fork() == 0) {
//       printf("B");
//       fflush(stdout);

//     } else {
//       wait(&status);
//       printf("C");
//       fflush(stdout);

//     }
//   } else {
//     printf("D");
//     fflush(stdout);

//   }
//   return 0;
// }

#include <stdio.h>
 #include <unistd.h>
 #include <fcntl.h>

int main(void) 
{ 
    int i; 
    // for(i=0; i<2; i++){ 
  fork(); 
        fork(); 
        printf("-"); 
    // } 

    return 0; 
}
// ————————————————
// 版权声明：本文为CSDN博主「DZ小明」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
// 原文链接：https://blog.csdn.net/sinat_36118270/java/article/details/75213178