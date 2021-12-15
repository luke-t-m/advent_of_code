import Data.List
import Data.List.Split
import Useful.Dictionary
import Data.Maybe
import qualified Data.Map as Map

look x p = fromJust (lookup x p)

look2 :: String -> [(String,String)] -> (Map.Map String Int) -> Int
look2 pair revrules i | (lookup pair revrules) /= Nothing && (lookup (fromJust (lookup pair revrules)) (dtl i)) /= Nothing = (look (look pair revrules) (dtl i))
                      | otherwise = 0

dtl = dictToList

step rules i = dict [ (pair, ((look pair (dtl i)) + (look2 pair revrules i))) | pair <- (map fst rules)]
 where revrules = map (\(s,t) -> (((head s):t),s)) rules

conv (x:[y]) = (x,y)

main :: IO ()
main = do
 input <- readFile "example.txt"
 let template = head (splitOn "\n\n" input)
 let rules = map (conv . splitOn " -> ") (tail (tail (lines input)))
 let pairs = dict [ (pair, 0) | pair <- (map fst rules)]
 let template = (dict [("NN",1),("NC",1),("CB",1)] #++ pairs)

-- print (map (\(s,t) -> (((head s):t),s)) rules)
 print (step rules (step rules template))

 print "done."



