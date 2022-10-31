class Test:
    '''
    '''
    def __init__(self):
        print('Test from Emstat Pico translator')


class CV:
    '''
    '''
    def __init__(self, Eini, Ev1, Ev2, Efin, sr, dE, nSweeps, sens,
                 folder, fileName, header, path_lib=None, qt=2, resistance=0):
        '''
            Potential based variables need to be changed to mV int(Eini*100).
            For some reason Pico does not accept not having prefix 
        '''
        Eini = int(Eini*1000)
        Ev1 = int(Ev1*1000)
        Ev2 = int(Ev2*1000)
        Efin = int(Efin*1000)
        sr = int(sr*1000)
        dE = int(dE*1000)
        self.text = ''
        self.ini = 'e\nvar c\nvar p\nvar a\n'
        self.pre_body = 'set_pgstat_mode 4\nset_autoranging ba 100n 5m' +\
                        '\nset_e '+ str(Eini) + 'm\ncell_on\ntimer_start'
        self.body = '\nmeas_loop_cv p c ' + str(Eini) + 'm ' + str(Ev1) + 'm ' +\
                    str(Ev2) + 'm ' + str(dE) + 'm ' + str(sr) +\
                    'm nscans(' + str(nSweeps) + ')\n\tpck_start\n\ttimer_get a' +\
                    '\n\tpck_add a\n\tpck_add p\n\tpck_add c\n\tpck_end\nendloop\n' + \
                    'on_finished:\ncell_off\n\n'
        self.text = self.ini + self.pre_body + self.body
        print(self.text)


    def bipot(self, E, sens):
        pass


class CA:
    '''
    '''
    def __init__(self, Estep, dt, ttot, sens, folder, fileName, header,
                 path_lib=None, qt=2):
        '''
        '''
        Estep = int(Estep*1000)
        dt = int(dt*1000)
        ttot = int(ttot*1000)
        self.text = ''
        self.ini = 'e\nvar p\nvar c\nvar a\n'
        self.pre_body = 'set_pgstat_mode 3\nset_autoranging ba 100n 5m' +\
                        '\nset_e ' + str(Estep) + 'm\ncell_on\ntimer_start'
        self.body = '\nmeas_loop_ca p c ' + str(Estep) + 'm ' + str(dt) +\
                    'm ' + str(ttot) + 'm\n\tpck_start\n\ttimer_get a\n\t' +\
                    'pck_add a\n\t' +\
                    'pck_add p\n\tpck_add c\n\tpck_end\n\tendloop' +\
                    '\non_finished:\ncell_off\n\n'
        self.text = self.ini + self.pre_body + self.body

    def bipot(self, E, sens):
        pass


class LSV:
    '''
    '''
    def __init__(self, Eini, Efin, sr, dE, sens, folder, fileName, header, 
                 path_lib=None, qt=2):
        Eini = int(Eini*1000)
        Efin = int(Efin*1000)
        sr = int(sr*1000)
        dE = int(dE*1000)
        self.text = ''
        self.ini = 'e\nvar c\nvar p\nvar a\n'
        self.pre_body = 'set_pgstat_mode 4\nset_autoranging ba 100n 5m' +\
                        '\nset_e '+ str(Eini) + 'm\ncell_on\ntimer_start'
        self.body = '\nmeas_loop_lsv p c ' + str(Eini) + 'm ' + str(Efin) + 'm ' +\
                    str(dE) + 'm ' + str(sr) +\
                    'm\n\tpck_start\n\ttimer_get a' +\
                    '\n\tpck_add a\n\tpck_add p\n\tpck_add c\n\tpck_end\nendloop\n' + \
                    'on_finished:\ncell_off\n\n'
        self.text = self.ini + self.pre_body + self.body
        print(self.text)

class OCP:
    '''
    '''
    def __init__(self, ttot, dt, folder, fileName, header, path_lib=None):
        dt = int(dt*1000)
        ttot = int(ttot*1000)
        self.text = ''
        self.ini = 'e\nvar p\nvar a\n'
        self.pre_body = 'set_pgstat_mode 4\ntimer_start\n'
        self.body = 'meas_loop_ocp p ' + str(dt) + 'm ' + str(ttot) + 'm '+\
                    '\n\tpck_start\n\ttimer_get a\n\tpck_add a\n\tpck_add p' +\
                    '\n\tpck_end\nendloop\non_finished:\ncell_off\n\n'
        self.text = self.ini + self.pre_body + self.body
        print(self.text)
        

        #'\n\tpck_start\n\ttimer_get a\n\tpck_add p\n\tpck_add a' +\
