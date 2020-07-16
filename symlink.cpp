#include <iostream>
#include <filesystem>
namespace fs = std::filesystem;
 
int main()
{
    fs::create_directories("sandbox/subdir");
    fs::create_symlink("target", "sandbox/sym1");
    fs::create_directory_symlink("subdir", "sandbox/sym2");
 
    for(auto it = fs::directory_iterator("sandbox"); it != fs::directory_iterator(); ++it)
        if(is_symlink(it->symlink_status()))
            std::cout << *it << "->" << read_symlink(*it) << '\n';
 
    fs::remove_all("sandbox");
}