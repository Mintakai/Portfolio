using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace station
{
    public class Root
    {
        public Data data { get; set; }
    }

    public class Values
    {
        public double windSpeed { get; set; }
        public double windDirection { get; set; }
        public double temperature { get; set; }
        public double cloudCover { get; set; }
        public int weatherCode { get; set; }
    }

    public class Interval
    {
        public DateTime startTime { get; set; }
        public Values values { get; set; }
    }

    public class Timeline
    {
        public string timestep { get; set; }
        public DateTime startTime { get; set; }
        public DateTime endTime { get; set; }
        public List<Interval> intervals { get; set; }
    }

    public class Data
    {
        public List<Timeline> timelines { get; set; }
    }
}
