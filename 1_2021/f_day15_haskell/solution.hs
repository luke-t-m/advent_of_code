import Data.List
import Data.List.Split




main :: IO ()
main = do
 input <- readFile "input.txt"

 putStr "Part 1: "
 print ""
 putStr "Part 2: "
 print ""
 print "done."



-- turn input into list of (pair, count) tuples
-- step through with set of rules- AB rule C produces pairs AC and CB
-- count letters at end by counting first letter of each pair?
