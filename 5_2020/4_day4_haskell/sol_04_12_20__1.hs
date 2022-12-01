import System.IO
import Data.List
import Data.List.Split


elemAll l x = and [ m `isInfixOf` x | m <- l ]

main :: IO ()
main = do
 input <- readFile "input.txt"
 let x = splitOn "\n\n" input
 print (length (filter (==True) (map (elemAll filtList) x)))
  where filtList = ["ecl:","pid:","eyr:","hcl:","byr:","iyr:","hgt:"]
