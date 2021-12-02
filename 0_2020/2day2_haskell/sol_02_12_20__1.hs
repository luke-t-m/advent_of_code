import System.IO
import Data.List
import Data.List.Split


countNum e x = length (filter (==e) x)

splitter x = delete "" (splitOneOf "- :" x)

checkerH x = checker (splitter x) 

checker :: [String] -> Bool
checker (a:b:c:d:_) = n >= read a && n <= read b where n = countNum (head c) d

main :: IO ()
main = do
 inputs <- readFile "input.txt"
 let lS = lines inputs
 print (length (filter (==True) (map checkerH lS)))

countNum e x = length (filter (==e) x)

splitter x = delete "" (splitOneOf "- :" x)

checkerH x = checker (splitter x) 

checker :: [String] -> Bool
checker (a:b:c:d:_) = (d!!((read a)-1) == head c) /= (d!!((read b)-1) == head c)
