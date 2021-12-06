import System.IO
import Data.List.Split


fishSim 0 f = f
fishSim t f = fishSim (t-1) (x ++ (concat (replicate (length f - length x) [6,8])))
 where x = filter (/=(-1)) (map (\y -> y-1) f)


tobfS x = [length (filter (==y) x) | y <- [0..8]]


bfishSim 0 f = f
bfishSim t f = bfishSim (t-1) ((tail (fst (splitAt 7 f))) ++ (f!!7 + head f) : f!!8 : [head f])


main :: IO ()
main = do
 input <- readFile "input.txt"
 let x = map read (splitOn "," input) :: [Int]
 print (length (fishSim 80 x))
 print (sum (bfishSim 256 (tobfS x)))
 print "done."
