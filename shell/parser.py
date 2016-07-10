import os
import time
from sys import exit
from lib.core.base import Base 

class Parser(Base):
    import optparse
    parser = optparse.OptionParser()
    parser.add_option('-p', '--payload', action="store")
    parser.add_option('-e', '--encoder', action="store", default="False")
    parser.add_option('-l','--list', action="store", default=True)
    parser.add_option('-n','--nc', action="store", default=True)

    #External sources(shellcode,py,asm encoders etc.)
    parser.add_option('-s', '--script', action="store")
    parser.add_option('-o', '--output', action="store", default=False)
    parser.add_option('-i', '--iteration', action="store")


    #Commandline shellcodes
    parser.add_option('--host', action="store")
    parser.add_option('--port', action="store")
    parser.add_option('--shellcode', action="store")
    parser.add_option('--url', action="store")
    parser.add_option('--message', action="store")
    parser.add_option('--file', action="store")
    parser.add_option('--filename', action="store")
    parser.add_option('--password', action="store")
    parser.add_option('--command', action="store")
    (options, args) = parser.parse_args()


    if options.list == "backdoors":
        from .core.backdoors import backdoorlist
        backdoorlist( require=False)
        exit()


    if options.list == "shellcodes":
        from .core.shellcodes import shellcodelist
        shellcodelist()
        exit()


    if options.list == "encoders":
        from .core.backdoors import encoderlist
        encoderlist( require=False)
        exit()


    if options.shellcode:
        if options.shellcode == "external":
            from .core.backdoors import encoderlist
            if options.encoder in encoderlist( require=True):
                module = Base.dynamicimport('shell.encoders.shellcode.'+(options.encoder.split("/")[-1]).replace(".py", ""))	
                if options.payload.startswith(r"\x"):
                    options.payload = options.payload.replace('"', "").strip()
                else:
                    try:
                        with open(options.payload, "r") as payload:
                            options.payload = binary2hex(payload.read())
                    except Exception as error:
                        exit("Unexpected error : ", error)

                data = module.prestart( options.payload.replace(r"\x", ""), options.iteration)
                if options.output:
                    with open(options.output, "w") as output:
                        output.write(data)
                else:
                    print("\n"+data)
                exit()

            else:
                exit("This encoder is not avaible.")

        else:
            from .core.shellcodes import shellcodelist
            shellcodelist = [x.lower() for x in shellcodelist( True)]
            if options.shellcode.lower() in shellcodelist:
                from .database.generator import generator
                choose, shellcode = options.shellcode.split("/")
                startime = time.time()
                output = ("\n"+generator( 
                    choose=choose, shellcode=shellcode, COMMAND=options.command,
                    FILE=options.file, FILENAME=options.filename, ip=options.host,
                    port=options.port, URL=options.url, PASSWORD=options.password
                )+"\n\n")

                print ("\nModule : {0}".format(options.shellcode))
                print ("Generate time : %.2f" % (float(startime)-(time.time())))
                print (output)
        exit()


    if options.list == "injectors":
        from .core.lists import injectorlist
        injectorlist()
        exit()

    elif options.nc == "netcat" or options.nc == "nc":
        from .Session.netcat import nc
        if options.port:
            nc( int(options.port))
        else:
            nc()
        exit()


    else:
        if options.payload:
            if options.host and options.port:
                from .core.backdoors import backdoorlist
                from .core.backdoors import encoderlist
                if options.payload in backdoorlist( require=True):
                    from .Session.generator import process
                    if options.encoder in encoderlist( True):
                        if "py" in options.encoder and "python" not in options.payload:
                            exit("\nThis encoder can not use with that payload\n")
                        if options.output:
                            process( options.payload, options.host, options.port, options.encoder, options.output)
                        else:
                            process( options.payload, options.host, options.port, options.encoder,True)
                else:
                    exit("\npython shellsploit  -p PAYLOAD -e ENCODER --host IP --port P0RT\n")
            else:
                exit("\npython shellsploit  -p PAYLOAD -e ENCODER --host IP --port P0RT\n")


        #For external scripts
        elif options.script:
            if options.encoder:
                from .core.backdoors import encoderlist
                if options.encoder in encoderlist( True):
                    if "/py/" in options.encoder:
                        from shell.encoders.py.starter import control
                    elif "/shellcode/" in options.encoder:
                        from shell.encoders.shellcode.starter import control
                    #elif options.script.endswith(".py") and "/py/" in options.encoder:
                    #elif options.script.endswith(".py") and "/py/" in options.encoder: 
                    try:
                        options.script = os.getcwd()+os.sep+options.script if "/" not in options.script else options.script
                        control(payload=options.encoder, files=[options.script], iteration=options.iteration)
                        if options.output:
                            if os.path.isdir("/".join(options.output.split("/")[:(len(options.output.split("/"))-1)])):
                                try:
                                    move(options.script, options.output)
                                except Exception as error:
                                    exit( "\nUnexpected error while moving file to target\n")
                                else:
                                    exit("\nFile encoded  : {0}\n".format( options.output)) 
                            else:
                                exit("\nYour target directory is not exist.\n")
                        else:
                            exit("\nFile encoded  : {0}\n".format( options.script))	
                    except Exception as error:
                        exit("\nUnexpected error : {0}\n".format( error))
                else:
                    exit("\npython shellsploit  --script YOURFILE --encoder ENCODERNAME\n")
            else:
                exit("\npython shellsploit  --script YOURFILE --encoder ENCODERNAME\n")	

Parser()
