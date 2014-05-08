'''
Created on Apr 5, 2014

@author: axxe
'''
from MultistagePipeline import MultistagePipeline

if __name__ == '__main__':
    arch = MultistagePipeline("./config.txt", "./inst.txt", "./reg.txt", "./instructionSet.txt", "./data.txt")
    arch.simulateInstructions()
    print "Execution Completed in Cycle: " + str(arch.executionCompleteCycle)
    print "Cache Hits: " + str(arch.instructionCacheHit) + " + " + str(arch.dataCacheHit)
    print "Cache Miss: " + str(arch.instructionCacheMiss) + " + " + str(arch.dataCacheMiss)
    arch.printOutputTable()
    # arch.writeOutputFile()
