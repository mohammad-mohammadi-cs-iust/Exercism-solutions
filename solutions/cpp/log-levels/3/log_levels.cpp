#include <string>


namespace log_line {

std::string message(const std::string& line) {
    std::size_t idx = line.find(" ") + 1;
    return line.substr(idx);
}

std::string log_level(const std::string& line) {
    std::size_t end = line.find("]");
    return line.substr(1, end - 1);
}

std::string reformat(const std::string& line) {
    return message(line) + " (" + log_level(line) + ")";
}

}  // namespace log_line