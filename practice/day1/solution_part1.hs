import System.IO
import Data.List.Unique


main :: IO ()
main = do
 inputs <- readFile "input.txt"
 let lS = lines inputs
     lI = map read lS
     lIR = map (\x -> 2020-x) lI
     lRep = repeated (lI ++ lIR)
 print (product lRep)
